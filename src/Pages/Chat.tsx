import React from 'react'
import {Card} from './Card'
import { Link } from 'wouter'
import styles from './Chat.module.scss'
import { useState } from 'react'
import cohere from 'cohere-ai'




export default  function(){
 



  const [person, setPerson] = useState({
    aitext: "Hello Nice to Meet You"
    
  });

  function handleaitextChange(e){
    setPerson({
      ...person,
      aitext: e.target.value
    });
  }

  function generate(){
    console.log(person.aitext)
    var userinput = person.aitext
    
   
    





    
    
    setPerson({
      ...person,
      aitext: "test"
    });
  }



  
 

    return (
      <>
      <Card>
      <p>
        {person.aitext}
      </p>
      <label>
        <input value={person.aitext} onChange={handleaitextChange}   ></input>
      </label>
      <button onClick={generate}>Submit</button>
      
     
      
      </Card>
      </>
    )
}