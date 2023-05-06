import React from 'react'
import { Route, Redirect, Switch } from 'wouter'
import { PageWrapper } from './PageWrapper'
import Home from "./Pages/Home" 
import Login from './Pages/Login'


export default function App (): JSX.Element {
    return (

        <>
        <Route path="/home">
            <PageWrapper  pageTheme={'home'}> 
                <Home/>
            </PageWrapper>
        </Route>
        <Route path="/login">
            <Login/>
        </Route>
        <Route path="/swap"></Route>
        </>
   )
  
  
  
    
}
