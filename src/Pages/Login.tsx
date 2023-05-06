import React from 'react'
import {Card} from './Card'
import { navigate } from 'wouter';
import { useNavigate } from "react-router-dom";


export default  function(): JSX.Element{
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
  console.log(json);
  // code goes here
  const history = useNavigate();
  history('/home');
 
 

  }


    return (
        <Card>
           <form method="post" onSubmit={handleSubmit} >
      <label>
        Text input: <input name="username" defaultValue="" />
      </label>
      <label>
        Text input: <input name="password" defaultValue="" />
      </label>
      <button type="submit">Submit form</button>
    </form>
        </Card>
      
   
    )
}