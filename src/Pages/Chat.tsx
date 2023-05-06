import React from 'react'
import {Card} from './Card'



export default  function(): JSX.Element{
    const DUMMY_DATA = [
        {
          senderId: "perborgen",
          text: "who'll win?"
        },
        {
          senderId: "janedoe",
          text: "who'll win?"
        }
      ]

      this.state = {
        messages: DUMMY_DATA
      }
 

    return (
        <Card>
          
        </Card>
    )
}