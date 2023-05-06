import React from 'react'
import {Card} from './Card'
import Messagelist from './Messageslist'
import { Link } from 'wouter'



export default  function(): JSX.Element{
  var messages = [
    {
      id:1,
      senderId: "perborgen",
      text: "whasdasdadsn?"
    },
    {
      id:2,
      senderId: "janedoe",
      text: "whasdasdasdin?"
    }
  ]

  function handleSubmit(e){
    e.preventDefault();
    const form = e.target;
    const formData = new FormData(form);
    fetch('/some-api', { method: form.method, body: formData });
    var  object = {};
    formData.forEach(function(value, key){
      object[key] = value;
  });
  var json = JSON.stringify(object);
  const oee = JSON.parse(json);
  console.log(oee.text);

  var input = {id:3, senderId: "user", text:oee.text}
  messages.push(input);



  
  }
 

    return (
      <Card>
      <div>
      {messages.map(name => {
        return (
          <div key = {name.id}> 
            <h2> name: {name.senderId}</h2>
            <h2> Message: {name.text}</h2>
            
          </div>
        );
      })}
      </div>
      <form method="post" onSubmit={handleSubmit} >
      <label>
        Text input: <input name="text" defaultValue="" />
      </label>
      
      <button type="submit">Submit form</button>
    </form>

      </Card>
    )
}