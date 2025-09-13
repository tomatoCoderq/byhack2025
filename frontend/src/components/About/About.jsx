import React from 'react'

export default function About({ t }) {
  return (
    <section className="about container">
      <h2>{t?.aboutTitle || 'О проекте'}</h2>
      <p>{t?.aboutText || 'Краткая информация о сайте.'}</p>
    </section>
  )
}

