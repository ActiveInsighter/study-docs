'use client';

import NextLink from 'next/link';
import { useRouter } from 'next/navigation';
import { type ComponentProps, useCallback, useRef } from 'react';

type IntentLinkProps = Omit<ComponentProps<'a'>, 'href'> & {
  href?: string;
  prefetch?: boolean | null;
};

/*
 * Next.js prefetches the full payload of every static route whose link scrolls
 * into view. Study pages can be large (pre-rendered KaTeX, word-card decks,
 * formula handbooks), and a directory such as the home page's mind map shows
 * dozens of them at once, so viewport prefetching would download most of the
 * site in the background. (The same component guards exam-docs, where one
 * page load once parsed about 18 MB of prefetched chapters on a phone.)
 *
 * This link prefetches only when a mouse hovers it, one route at a time,
 * usually well before the click. Touch gets no prefetch: the click follows
 * pointerdown within milliseconds, so a prefetch started there never finishes
 * first and only made the phone download and parse the page twice. An
 * explicit `prefetch` prop still wins.
 */
export function IntentLink({ href = '#', prefetch, onPointerEnter, ...props }: IntentLinkProps) {
  const router = useRouter();
  const warmed = useRef<string | null>(null);
  const warm = useCallback(() => {
    if (warmed.current === href || !href.startsWith('/')) return;
    warmed.current = href;
    router.prefetch(href);
  }, [href, router]);

  return (
    <NextLink
      href={href}
      prefetch={prefetch ?? false}
      onPointerEnter={(event) => {
        if (event.pointerType === 'mouse') warm();
        onPointerEnter?.(event);
      }}
      {...props}
    />
  );
}
