import type { Tone } from './content';

/* Plain data passed from the home page's server components to its client islands. */

export interface StudySection {
  name: string;
  href: string;
  pages: number;
}

export interface StudyModule {
  /** Folder name under content/docs, e.g. "math". */
  key: string;
  name: string;
  href: string;
  tone: Tone;
  pages: number;
  sections: StudySection[];
}

export interface WordCard {
  word: string;
  phonetic: string;
  label: string;
  meanings: { pos: string; text: string }[];
  example: { text: string; translation: string } | null;
}
