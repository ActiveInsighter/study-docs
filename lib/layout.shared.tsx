import type {
  BaseLayoutProps,
  LinkItemType,
} from 'fumadocs-ui/layouts/shared';
import { siteConfig } from './site-config';
import { SiteIcon } from '@/components/site-icon';

export function baseOptions(): BaseLayoutProps {
  return {
    nav: {
      title: (
        <span className="inline-flex items-center gap-2.5">
          <SiteIcon size={24} />
          <span>{siteConfig.name}</span>
        </span>
      ),
    },
    githubUrl: siteConfig.repository.url,
  };
}

export const linkItems: LinkItemType[] = [
  {
    type: 'main',
    text: '学习',
    url: '/docs/politics',
  },
  {
    type: 'main',
    text: 'Blog',
    url: '/blog',
  },
];
