'use client';

import { Search } from 'lucide-react';
import { useSearchContext } from 'fumadocs-ui/contexts/search';
import { useSyncExternalStore } from 'react';

const noop = () => () => {};
const isApple = () => /Mac|iPhone|iPad/u.test(navigator.platform || navigator.userAgent);

/** Opens the site's search dialog (the same one as Ctrl/⌘ K). */
export function SearchButton({ className, kbdClassName }: { className?: string; kbdClassName?: string }) {
  const { setOpenSearch, enabled } = useSearchContext();
  const apple = useSyncExternalStore(noop, isApple, () => false);
  if (!enabled) return null;

  return (
    <button type="button" className={className} onClick={() => setOpenSearch(true)}>
      <Search aria-hidden="true" />
      搜索笔记
      <kbd className={kbdClassName}>{apple ? '⌘' : 'Ctrl'} K</kbd>
    </button>
  );
}
