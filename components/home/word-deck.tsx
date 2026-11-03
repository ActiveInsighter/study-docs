'use client';

import { RotateCw } from 'lucide-react';
import { useState } from 'react';
import type { WordCard } from '@/lib/home/types';
import styles from './specimens.module.css';

/** A few real vocabulary cards: tap to flip, then move on to the next one. */
export function WordDeck({ words }: { words: WordCard[] }) {
  const [index, setIndex] = useState(0);
  const [flipped, setFlipped] = useState(false);
  const card = words[index];
  if (!card) return null;

  const next = () => {
    setFlipped(false);
    setIndex((value) => (value + 1) % words.length);
  };

  return (
    <div className={styles.deck}>
      <button
        type="button"
        className={styles.card}
        data-flipped={flipped ? '' : undefined}
        aria-pressed={flipped}
        aria-label={flipped ? `${card.word}，背面：释义和例句。点按翻回正面` : `${card.word}，点按翻到背面看释义`}
        onClick={() => setFlipped((value) => !value)}
      >
        <span className={styles.cardInner}>
          <span className={styles.cardFront} aria-hidden={flipped}>
            <span className={styles.cardLabel}>{card.label}</span>
            <span className={styles.cardWord}>{card.word}</span>
            <span className={styles.cardPhonetic}>{card.phonetic}</span>
            <span className={styles.cardHint}>
              <RotateCw aria-hidden="true" />
              点按翻面
            </span>
          </span>
          <span className={styles.cardBack} aria-hidden={!flipped}>
            <span className={styles.cardMeanings}>
              {card.meanings.map((meaning) => (
                <span key={meaning.pos + meaning.text}>
                  <i>{meaning.pos}</i>
                  {meaning.text}
                </span>
              ))}
            </span>
            {card.example && (
              <span className={styles.cardExample}>
                <span lang="en">{card.example.text}</span>
                <span>{card.example.translation}</span>
              </span>
            )}
          </span>
        </span>
      </button>
      <div className={styles.deckBar}>
        <span className={styles.deckCount}>
          {index + 1} / {words.length}
        </span>
        <button type="button" className={styles.textButton} onClick={next}>
          下一张
        </button>
      </div>
    </div>
  );
}
