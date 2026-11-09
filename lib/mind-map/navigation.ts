/** Chapter guide first, then its sections in numeric order (2 before 10). */
export function compareMindMapPaths(a: string, b: string) {
  const key = (path: string) => {
    const parts = path.split('/');
    const filename = parts.at(-1) ?? '';
    // A chapter's index lives beside its numbered sections and comes first.
    return /^(\d{2})-(?:(\d+)-)?/.exec(
      /^index\.mdx?$/.test(filename) ? parts.at(-2) ?? '' : filename,
    );
  };
  const left = key(a);
  const right = key(b);
  if (left && right) {
    const chapter = Number(left[1]) - Number(right[1]);
    if (chapter) return chapter;
    const section = Number(left[2] ?? 0) - Number(right[2] ?? 0);
    if (section) return section;
  }
  return a.localeCompare(b, undefined, { numeric: true });
}
