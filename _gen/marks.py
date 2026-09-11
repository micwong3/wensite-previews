def mark_svg(lead):
    slug = lead["slug"]; cat = lead["cat"]
    if cat == "spa":
        return '<svg class="mark" viewBox="0 0 64 64" aria-hidden="true"><circle cx="32" cy="32" r="30" fill="currentColor" opacity=".12"/><path fill="currentColor" d="M40 12c-12 4-20 16-20 28 0 2.2.3 4.3.8 6.3C14.5 41 12 34.8 12 28 12 16.4 20.8 7.2 32 5c0 0-1 3.5 0 7 1 3.5 5.5 5.8 8 0z"/><circle cx="42" cy="22" r="3" fill="currentColor"/></svg>'
    if cat == "vet":
        return '<svg class="mark" viewBox="0 0 64 64" aria-hidden="true"><ellipse cx="20" cy="18" rx="8" ry="11" fill="currentColor"/><ellipse cx="44" cy="18" rx="8" ry="11" fill="currentColor"/><ellipse cx="12" cy="36" rx="7" ry="9" fill="currentColor"/><ellipse cx="52" cy="36" rx="7" ry="9" fill="currentColor"/><ellipse cx="32" cy="40" rx="14" ry="16" fill="currentColor"/></svg>'
    if cat == "auto":
        return '<svg class="mark mark-wide" viewBox="0 0 120 36" aria-hidden="true"><rect width="120" height="36" rx="4" fill="currentColor"/><text x="60" y="24" text-anchor="middle" font-family="Oswald,sans-serif" font-size="16" font-weight="700" fill="#111">OMEGA MP</text></svg>'
    if cat == "legal" and "bacharach" in slug:
        return '<svg class="mark" viewBox="0 0 72 72" aria-hidden="true"><path fill="currentColor" d="M36 6 L60 18 V38 C60 52 48 62 36 66 C24 62 12 52 12 38 V18 Z"/><path fill="#fff" d="M36 16 L50 24 V38 C50 46 42 52 36 55 C30 52 22 46 22 38 V24 Z" opacity=".9"/></svg>'
    if cat == "legal":
        return '<svg class="mark mark-wide" viewBox="0 0 80 40" aria-hidden="true"><text x="0" y="28" font-family="Source Serif 4,Georgia,serif" font-size="26" font-weight="700" fill="currentColor">Capstone</text><rect y="32" width="78" height="2" fill="currentColor"/></svg>'
    if cat == "plumbing":
        return '<svg class="mark" viewBox="0 0 64 64" aria-hidden="true"><path fill="currentColor" d="M14 10h12v8H14zm24 0h12v8H38zM10 22h44v8H38v24H26V30H10z"/></svg>'
    if cat == "hvac" and "quality" in slug:
        return '<svg class="mark" viewBox="0 0 64 64" aria-hidden="true"><circle cx="32" cy="32" r="10" fill="currentColor"/><g stroke="currentColor" stroke-width="4" stroke-linecap="round" fill="none"><path d="M32 6v10M32 48v10M6 32h10M48 32h10M14 14l7 7M43 43l7 7M50 14l-7 7M21 43l-7 7"/></g></svg>'
    if cat == "hvac":
        return '<svg class="mark" viewBox="0 0 64 64" aria-hidden="true"><path fill="currentColor" d="M8 36c8-16 16-24 24-24s16 8 24 24c-8 4-16 6-24 6s-16-2-24-6z"/><path fill="currentColor" opacity=".45" d="M12 44c6-4 14-6 20-6s14 2 20 6c-6 8-12 12-20 12s-14-4-20-12z"/></svg>'
    if "nations" in slug:
        return '<svg class="mark" viewBox="0 0 64 64" aria-hidden="true"><path fill="currentColor" d="M32 8c6 10 18 14 18 28a18 18 0 1 1-36 0c0-14 12-18 18-28z"/><rect x="29" y="40" width="6" height="16" rx="2" fill="currentColor"/></svg>'
    return '<svg class="mark mark-wide" viewBox="0 0 140 36" aria-hidden="true"><text x="0" y="26" font-family="Cormorant Garamond,Georgia,serif" font-size="28" font-weight="700" fill="currentColor">Bank Dental</text></svg>'
