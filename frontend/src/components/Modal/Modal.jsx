import React, { useEffect, useRef } from 'react'
import styles from './Modal.module.css'
import Button from '../Button/Button'

export default function Modal({ item, lang = 'ru', t, onClose, onPlay }) {
  const dialogRef = useRef(null)

  useEffect(() => {
    const onKey = (e) => { if (e.key === 'Escape') onClose() }
    window.addEventListener('keydown', onKey)
    return () => window.removeEventListener('keydown', onKey)
  }, [onClose])

  return (
    <div className="overlay" onClick={onClose}>
      <section
        className="modal"
        role="dialog"
        aria-modal="true"
        aria-labelledby={`modal-title-${item.id}`}
        onClick={(e) => e.stopPropagation()}
        ref={dialogRef}
      >
        <div className="modal__left">
          <img className="modal__image" src={item.image} alt={item.title?.[lang] || ''} />
        </div>
        <div className="modal__right">
          <div className="modal__header">
            <h2 id={`modal-title-${item.id}`} className={styles.modal__title}>{item.title?.[lang] || ''}</h2>
            <button className="modal__close" onClick={onClose} aria-label={t?.close || 'Close'}>×</button>
          </div>
          <div className="modal__body" role="region" aria-label="Текстовое описание с прокруткой">
            <div className="info-list">
              <div className={styles["info-item"]}>
                <span className={styles['info-label']}>{t?.historyLabel || 'ИСТОРИЯ'}:</span>
                <span className={styles['info-text']}>{item.details?.history?.[lang] || item.description?.[lang] || ''}</span>
              </div>
              <div className={styles["info-item"]}>
                <span className={styles['info-label']}>{t?.habitatLabel || 'МЕСТО ОБИТАНИЯ'}:</span>
                <span className={styles['info-text']}>{item.details?.habitat?.[lang] || '...'}</span>
              </div>
              <div className={styles["info-item"]}>
                <span className={styles['info-label']}>{t?.featuresLabel || 'ОСОБЕННОСТИ'}:</span>
                <span className={styles['info-text']}>{item.details?.features?.[lang] || '...'}</span>
              </div>
            </div>
            <div className="modal__spacer" aria-hidden="true" />
            <Button className={styles['button_play']} onClick={() => onPlay?.(item)}>{t?.play || 'Играть'}</Button>
          </div>
        </div>
      </section>
    </div>
  )
}

