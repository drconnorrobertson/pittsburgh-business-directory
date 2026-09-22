'use strict';
const queryInput = document.querySelector('#query');
const resultsEl = document.querySelector('#results');
const countEl = document.querySelector('#count');
const q = new URLSearchParams(location.search).get('q') || '';
queryInput.value = q;
function render(profiles, term) {
  const tokens = term.toLocaleLowerCase().trim().split(/\s+/).filter(Boolean);
  const matches = profiles.filter(p => tokens.every(t => (p.name + ' ' + p.description).toLocaleLowerCase().includes(t)));
  resultsEl.replaceChildren();
  countEl.textContent = matches.length + (matches.length === 1 ? ' profile' : ' profiles') + (term ? ' for “' + term + '”' : '');
  for (const item of matches.slice(0, 100)) {
    const article = document.createElement('article');
    article.className = 'result';
    const h2 = document.createElement('h2');
    const link = document.createElement('a');
    link.href = item.url;
    link.textContent = item.name;
    h2.append(link);
    const p = document.createElement('p');
    p.textContent = item.description;
    article.append(h2, p);
    resultsEl.append(article);
  }
  if (matches.length > 100) {
    const note = document.createElement('p');
    note.textContent = 'Showing the first 100 matches. Narrow your search to see more.';
    resultsEl.after(note);
  }
}
fetch('./profiles.json').then(r => {
  if (!r.ok) throw new Error('Search index unavailable');
  return r.json();
}).then(profiles => render(profiles, q)).catch(() => {
  countEl.textContent = 'Search is temporarily unavailable. Browse categories from the homepage.';
});
