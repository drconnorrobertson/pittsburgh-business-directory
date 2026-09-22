'use strict';
for (const form of document.querySelectorAll('form[data-email-draft]')) {
  const button = form.querySelector('button[type=submit]');
  if (button) button.textContent = form.dataset.emailDraft === 'business' ? 'Prepare submission email' : 'Prepare message email';
  form.addEventListener('submit', event => {
    event.preventDefault();
    if (!form.reportValidity()) return;
    const data = [...new FormData(form).entries()];
    const subject = form.dataset.emailDraft === 'business'
      ? 'Business profile submission: ' + (form.elements.business_name?.value || '')
      : 'Directory contact: ' + (form.elements.subject?.value || '');
    const body = data.map(([key, value]) =>
      key.replaceAll('_', ' ').replace(/\b\w/g, char => char.toUpperCase()) + ': ' + value
    ).join('\n\n');
    let panel = form.nextElementSibling;
    if (!panel || !panel.classList.contains('email-draft')) {
      panel = document.createElement('section');
      panel.className = 'email-draft';
      panel.style.cssText = 'margin:24px 0;padding:24px;border:2px solid #C8A040;border-radius:8px;background:#faf8f0;color:#222';
      form.after(panel);
    }
    panel.replaceChildren();
    const heading = document.createElement('h2');
    heading.textContent = 'Your email draft is ready';
    const instruction = document.createElement('p');
    instruction.textContent = 'Copy the full message below, open your email app, paste it into the email, and send it. This website has not sent or saved your information.';
    const draft = document.createElement('textarea');
    draft.readOnly = true;
    draft.value = body;
    draft.setAttribute('aria-label', 'Email draft');
    draft.style.cssText = 'width:100%;min-height:220px;padding:12px;line-height:1.5';
    const copy = document.createElement('button');
    copy.type = 'button';
    copy.textContent = 'Copy message';
    copy.addEventListener('click', async () => {
      try {
        await navigator.clipboard.writeText(body);
        copy.textContent = 'Copied';
      } catch {
        draft.select();
        copy.textContent = 'Select and copy the text above';
      }
    });
    const email = document.createElement('a');
    email.href = 'mailto:hello@pittsburghbusinessdirectory.com?subject=' + encodeURIComponent(subject);
    email.textContent = 'Open email app →';
    email.style.cssText = 'display:inline-block;margin-left:16px;color:#7f5200;font-weight:700';
    panel.append(heading, instruction, draft, copy, email);
    panel.scrollIntoView({behavior:'smooth', block:'start'});
  });
}
