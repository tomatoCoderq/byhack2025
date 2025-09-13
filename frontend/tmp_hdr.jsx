import React from 'react'
import Button from '../Button/Button'
import styles from './Header.module.css';

export default function Header({ lang = 'ru', t, onToggleLang }) {
  const flagSrc = lang === 'ru' ? '/russia.png' : '/tatarstan.png'
  const aria = lang === 'ru' ? 'Переключить на татарский' : 'Переключить на русский'
  return (
    <header className="header">
      <div className="header__inner">
        <div className="header__top">
          <Button className="button_left">{t.button1?.[lang] || ''}</Button>
          <h1 className={styles["title_header"]}>ШУРАЙ</h1>
          <Button className="button_right">О проекте</Button>
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


