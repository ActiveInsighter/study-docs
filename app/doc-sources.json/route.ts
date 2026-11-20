import { getSourceTree } from '@/lib/doc-sources.server';

export const revalidate = false;
export const dynamic = 'force-static';

export function GET() {
  return Response.json(getSourceTree(), {
    headers: { 'Cache-Control': 'public, max-age=0, must-revalidate' },
  });
}
