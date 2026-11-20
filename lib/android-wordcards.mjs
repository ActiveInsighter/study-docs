import vm from 'node:vm';
import { kaoyanWords } from '../data/vocabulary/kaoyan-word-cards.mjs';
import { phraseWords } from '../data/vocabulary/phrase-cards.mjs';
import { supplementalWords } from '../data/vocabulary/supplemental-word-cards.mjs';

const VOCAB_SOURCES = {
  kaoyanWords,
  supplementalWords,
  phraseWords,
};

function sanitizeWordCard(item) {
  if (!item || typeof item !== 'object' || typeof item.word !== 'string') return null;
  const meanings = Array.isArray(item.meanings)
    ? item.meanings
        .filter((m) => m && typeof m.text === 'string')
        .map((m) => ({
          ...(m.pos ? { pos: String(m.pos) } : {}),
          text: String(m.text),
          ...(m.key ? { key: true } : {}),
          ...(m.grammar ? { grammar: String(m.grammar) } : {}),
          ...(m.phrase ? { phrase: true } : {}),
        }))
    : [];
  const senses = Array.isArray(item.senses)
    ? item.senses
        .filter((s) => s && typeof s.gloss === 'string')
        .map((s) => ({
          gloss: String(s.gloss),
          count: Number.isFinite(Number(s.count)) ? Math.max(0, Number(s.count)) : 0,
          ...(s.percentage !== undefined && Number.isFinite(Number(s.percentage))
            ? { percentage: Number(s.percentage) }
            : {}),
          ...(Array.isArray(s.examples)
            ? {
                examples: s.examples
                  .filter((e) => e && typeof e.text === 'string')
                  .map((e) => ({
                    text: String(e.text),
                    translation: typeof e.translation === 'string' ? e.translation : '',
                  })),
              }
            : {}),
        }))
    : undefined;

  return {
    word: item.word,
    ...(item.phonetic ? { phonetic: String(item.phonetic) } : {}),
    ...(item.label ? { label: String(item.label) } : {}),
    meanings,
    ...(senses?.length ? { senses } : {}),
  };
}

/**
 * Evaluate a `<WordCards words={...} />` expression in a restricted VM context
 * with only the vocabulary arrays exposed, and serialize to a `:::wordcards`
 * Android Markdown container.
 */
export function resolveWordCardsExpression(expression) {
  if (!expression || typeof expression !== 'string') return null;
  try {
    const context = vm.createContext({ ...VOCAB_SOURCES });
    const raw = vm.runInContext(`(${expression})`, context, { timeout: 100 });
    if (!Array.isArray(raw) || raw.length === 0) return null;
    const words = raw.map(sanitizeWordCard).filter(Boolean);
    if (words.length === 0) return null;
    return `\n\n:::wordcards\n~~~json\n${JSON.stringify(words)}\n~~~\n:::\n\n`;
  } catch {
    return null;
  }
}
