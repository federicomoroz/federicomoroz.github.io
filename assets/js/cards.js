// Project cards: the status LEDs power on one by one the first time the grid is
// seen, and on touch screens the live preview plays while a card is on screen.
(function ()
{
    'use strict';

    var cards = Array.prototype.slice.call(document.querySelectorAll('.pcard'));
    if (!cards.length)
        return;

    if (!('IntersectionObserver' in window))
    {
        cards.forEach(function (c) { c.classList.add('on'); });
        return;
    }

    var power = new IntersectionObserver(function (entries)
    {
        var batch = entries.filter(function (e) { return e.isIntersecting; });
        batch.forEach(function (entry, i)
        {
            setTimeout(function () { entry.target.classList.add('on'); }, 180 * i);
            power.unobserve(entry.target);
        });
    }, { threshold: 0.35 });

    cards.forEach(function (c) { power.observe(c); });

    // Without hover, the live preview plays while the card is mostly on screen.
    if (window.matchMedia('(hover: none)').matches)
    {
        var player = new IntersectionObserver(function (entries)
        {
            entries.forEach(function (entry)
            {
                entry.target.classList.toggle('playing', entry.intersectionRatio > 0.6);
            });
        }, { threshold: [0, 0.6, 1] });

        cards.forEach(function (c) { player.observe(c); });
    }
})();
