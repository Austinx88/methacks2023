import React from 'react'
import { Route, Redirect, Switch } from 'wouter'
import { PageWrapper } from './PageWrapper'
import Home from "./Pages/Home" 
import Login from './Pages/Login'
import Chat from './Pages/Chat'



export default function App (): JSX.Element {
    return (

        <>
        <Switch>
        <Route path="/home">
            <PageWrapper  pageTheme={'light'}> 
                <Home/>
            </PageWrapper>
        </Route>

        <Route path="/login">
            <PageWrapper pageTheme={'light'}><Login/></PageWrapper>
            
        </Route>

        <Route path="/chat">
        <PageWrapper pageTheme={'light'}><Chat/></PageWrapper>
        </Route>
        </Switch>
        </>
   )
  
  
  
    
}
