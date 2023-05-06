import React from 'react'
import {Card} from './Card'
import styles from './Home.module.scss'
import logo from "../Assets/rizzify.png"
import { Link } from 'wouter'


export default  function(): JSX.Element{
  const handleClick = (e) => {
    e.preventDefault();

  }
 

    return (
        <Card>
          <img className={styles.img} src = { logo} />
          <div className= {styles.card}></div>
          
          <Link className ={styles.button} to='/login'>Chat </Link>

          <button className={styles.button}onClick={handleClick}>
            Next 
          </button>
        </Card>
    )
}