// The hero lab: run a real chargeback case through the schematic.
//
// The cases and their texts come from _data/lab.yml (window.__LAB__). There are
// two schematics, horizontal and vertical; the one on screen is the one that
// gets animated, each with its own geometry below.
(function ()
{
    'use strict';

    var D = window.__LAB__;
    var root = document.querySelector('.lab');
    if (!D || !root)
        return;

    var ORDER = ['case', 'rag', 'model', 'rules'];

    // Where the signal travels between stages, per orientation.
    var GEOMETRY = {
        'lab-h-': {
            start: [38, 150],
            legs: { case: [[38, 150], [110, 150]], rag: [[270, 150], [320, 150]], model: [[480, 150], [530, 150]], rules: [[690, 150], [740, 150]] },
            branch: {
                approve: [[900, 150], [960, 150], [960, 70], [1006, 70]],
                human:   [[900, 150], [960, 150], [1006, 150]],
                reject:  [[900, 150], [960, 150], [960, 230], [1006, 230]]
            }
        },
        'lab-v-': {
            start: [180, 37],
            legs: { case: [[180, 60], [180, 90]], rag: [[180, 166], [180, 196]], model: [[180, 272], [180, 302]], rules: [[180, 378], [180, 408]] },
            branch: {
                approve: [[180, 500], [180, 536], [60, 536], [60, 570]],
                human:   [[180, 500], [180, 536], [180, 570]],
                reject:  [[180, 500], [180, 536], [300, 536], [300, 570]]
            }
        }
    };

    var readout = root.querySelector('.readout');
    var buttons = Array.prototype.slice.call(root.querySelectorAll('.case'));
    var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    var run = 0;

    function visibleSchematic()
    {
        var all = root.querySelectorAll('.sch');
        for (var i = 0; i < all.length; i++)
        {
            if (getComputedStyle(all[i]).display !== 'none')
                return all[i];
        }
        return all[0];
    }

    function wait(ms)
    {
        return new Promise(function (r) { setTimeout(r, reduced ? 0 : ms); });
    }

    function travel(signal, points, speed)
    {
        if (reduced)
            return Promise.resolve();

        var segs = [], total = 0;
        for (var i = 1; i < points.length; i++)
        {
            var dx = points[i][0] - points[i - 1][0], dy = points[i][1] - points[i - 1][1];
            var len = Math.sqrt(dx * dx + dy * dy);
            segs.push({ a: points[i - 1], b: points[i], len: len });
            total += len;
        }

        var duration = total / speed * 1000, start = null;
        signal.setAttribute('opacity', '1');

        return new Promise(function (resolve)
        {
            function frame(t)
            {
                if (start === null) start = t;
                var d = Math.min(1, (t - start) / duration) * total;
                for (var k = 0; k < segs.length; k++)
                {
                    if (d <= segs[k].len || k === segs.length - 1)
                    {
                        var f = segs[k].len ? Math.min(1, d / segs[k].len) : 1;
                        signal.setAttribute('cx', segs[k].a[0] + (segs[k].b[0] - segs[k].a[0]) * f);
                        signal.setAttribute('cy', segs[k].a[1] + (segs[k].b[1] - segs[k].a[1]) * f);
                        break;
                    }
                    d -= segs[k].len;
                }
                if (t - start < duration)
                    requestAnimationFrame(frame);
                else
                {
                    signal.setAttribute('opacity', '0');
                    resolve();
                }
            }
            requestAnimationFrame(frame);
        });
    }

    function line(title, text, kind)
    {
        var li = document.createElement('li');
        if (kind) li.className = kind;
        var b = document.createElement('b');
        b.textContent = title;
        var span = document.createElement('span');
        span.textContent = text;
        li.appendChild(b);
        li.appendChild(span);
        readout.appendChild(li);
    }

    function reset()
    {
        readout.innerHTML = '';
        root.querySelectorAll('.stage, .out').forEach(function (g) { g.classList.remove('lit', 'fault', 'on', 'approve', 'human', 'reject'); });
        root.querySelectorAll('.trace').forEach(function (p) { p.classList.remove('hot'); });
    }

    async function play(name)
    {
        var my = ++run;
        var c = D.cases[name];
        var svg = visibleSchematic();
        var prefix = svg.getAttribute('data-prefix');
        var geo = GEOMETRY[prefix];
        var signal = svg.querySelector('.signal');

        reset();
        buttons.forEach(function (b) { b.setAttribute('aria-pressed', String(b.dataset.case === name)); });

        for (var i = 0; i < ORDER.length; i++)
        {
            var id = ORDER[i];
            await travel(signal, geo.legs[id], 420);
            if (my !== run) return;

            var failed = c.fail === id;
            root.querySelectorAll('[id$="-s-' + id + '"]').forEach(function (g) { g.classList.add(failed ? 'fault' : 'lit'); });
            line(D.stages[id], c.steps[id], failed ? 'bad' : '');
            await wait(900);
            if (my !== run) return;
        }

        await travel(signal, geo.branch[c.out], 420);
        if (my !== run) return;

        // Light the result on both schematics, so resizing keeps the state.
        root.querySelectorAll('[id$="-t-' + c.out + '"]').forEach(function (p) { p.classList.add('hot'); });
        root.querySelectorAll('[id$="-o-' + c.out + '"]').forEach(function (g) { g.classList.add('on', c.out); });
        line(D.outputs[c.out], c.end, 'result ' + c.out);
    }

    buttons.forEach(function (b)
    {
        b.addEventListener('click', function () { play(b.dataset.case); });
    });

    // One orchestrated moment: the first case runs by itself, once, when the
    // lab first comes into view.
    var first = Object.keys(D.cases)[0];
    if (!('IntersectionObserver' in window))
    {
        play(first);
        return;
    }

    var seen = new IntersectionObserver(function (entries)
    {
        if (entries[0].isIntersecting && run === 0)
        {
            setTimeout(function () { if (run === 0) play(first); }, 500);
            seen.disconnect();
        }
    }, { threshold: 0.4 });
    seen.observe(root.querySelector('.board'));
})();
