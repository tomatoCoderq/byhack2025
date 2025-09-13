import React from 'react'
import styles from './Card.module.css';

export default function Card({ item, lang = 'ru', t, onClick }) {
  const title = item.title?.[lang] || ''
  return (
    <button
      className="card"
      onClick={onClick}
      aria-label={`${t?.openCardPrefix || ''}: ${title}`.trim()}
    >
      <div className="card__image-wrapper">
        <img className="card__image" src={item.image} alt={title} loading="lazy" />
      </div>
      <div className="card__content">
        <h3 className={styles["card__title"]}>{title}</h3>
      </div>
    </button>
  )
}

