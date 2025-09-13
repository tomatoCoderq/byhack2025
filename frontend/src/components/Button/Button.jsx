import React from 'react'
import styles from './Button.module.css'

export default function Button({
  children,
  type = 'button',
  side,
  color = '#0b6a52',
  className,
  ...rest
}) {
  const wantsLeft = typeof className === 'string' && className.split(/\s+/).includes('button_left')
  const wantsRight = typeof className === 'string' && className.split(/\s+/).includes('button_right')
  const sideClass = side === 'right' || wantsRight ? styles.button_right : (side === 'left' || wantsLeft ? styles.button_left : '')
  const cls = [styles.button, sideClass, className]
    .filter(Boolean)
    .join(' ')

  return (
    <button
      type={type}
      className={cls}
      style={{ '--btn-color': color }}
      {...rest}
    >
      {children}
    </button>
  )
}
