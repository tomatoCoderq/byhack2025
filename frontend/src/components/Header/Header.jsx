import React from 'react'
import Button from '../Button/Button'
import styles from './Header.module.css'

export default function Header({ lang = 'ru', t, onToggleLang, userName, onGoCharacters, onGoAbout }) {
  const flagSrc = lang === 'ru' ? '/russia.png' : '/tatarstan.png'
  const aria = lang === 'ru' ? 'Переключить на татарский' : 'Переключить на русский'
  return (
    <header className="header">
      <div className="header__inner">
        {userName && (
          <div className="header__user" title={userName}>{userName}</div>
        )}
        <div className="header__top">
          <Button side="left" onClick={onGoCharacters}>{t?.button1 || 'ПЕРСОНАЖИ'}</Button>
          <h1 className={styles.title_header}>SHURAY</h1>
          <Button side="right" onClick={onGoAbout}>{t?.button2 || 'О ПРОЕКТЕ'}</Button>
        </div>
        <button
          className="lang-toggle"
          type="button"
          onClick={onToggleLang}
          aria-label={aria}
          title={aria}
        >
          <img className="lang-flag" src={flagSrc} alt="" aria-hidden="true" />
        </button>
      </div>
    </header>
  )
}

