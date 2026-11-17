// Domain-tag filter of the projects and tools pages: the chosen tag leaves only
// the cards that have it, hides the blocks left empty and goes in the address
// (?tag=<id>) so a filtered page can be shared. A card's own tag applies it too.
(function ()
{
    'use strict';

    var bar = document.querySelector('.tag-filter');
    if (!bar)
        return;

    var buttons = Array.prototype.slice.call(bar.querySelectorAll('button[data-tag]'));
    var cards = Array.prototype.slice.call(document.querySelectorAll('.pcard'));
    var groups = Array.prototype.slice.call(document.querySelectorAll('[data-filter-group]'));
    var known = buttons.map(function (b) { return b.getAttribute('data-tag'); });

    function hasTag(card, tag)
    {
        return (' ' + (card.getAttribute('data-tags') || '') + ' ').indexOf(' ' + tag + ' ') !== -1;
    }

    function apply(tag)
    {
        if (known.indexOf(tag) === -1)
            tag = '';

        buttons.forEach(function (b)
        {
            b.setAttribute('aria-pressed', String(b.getAttribute('data-tag') === tag));
        });
        cards.forEach(function (card)
        {
            card.hidden = tag !== '' && !hasTag(card, tag);
        });
        groups.forEach(function (group)
        {
            group.hidden = tag !== '' && !group.querySelector('.pcard:not([hidden])');
        });

        var url = new URL(window.location.href);
        if (tag)
            url.searchParams.set('tag', tag);
        else
            url.searchParams.delete('tag');
        window.history.replaceState(null, '', url.pathname + url.search + url.hash);
    }

    bar.addEventListener('click', function (event)
    {
        var button = event.target.closest('button[data-tag]');
        if (button)
            apply(button.getAttribute('data-tag'));
    });

    // A tag on a card filters this same page, when this page has that filter.
    document.addEventListener('click', function (event)
    {
        var link = event.target.closest('.pcard-tags a[data-tag]');
        if (!link || known.indexOf(link.getAttribute('data-tag')) === -1)
            return;
        event.preventDefault();
        apply(link.getAttribute('data-tag'));
        bar.scrollIntoView({ block: 'nearest', behavior: 'smooth' });
    });

    bar.hidden = false;
    apply(new URLSearchParams(window.location.search).get('tag') || '');
})();
