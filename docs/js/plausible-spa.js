// Re-fire a pageview on MkDocs Instant Navigation route changes
if (typeof document$ !== 'undefined') {
  document$.subscribe(() => {
    if (window.plausible) window.plausible('pageview');
  });
}
