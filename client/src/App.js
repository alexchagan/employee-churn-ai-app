import React, { useState, useEffect } from 'react'
// useState -> data retrieved from the backend
// useEffect -> fetch the backend api on the first render
import InputForm from './components/InputForm'
import "./App.css"


function App() {

  const [response, setResponse] = useState(null)
 
  const handleSubmit = (values) =>
  {
    console.log({ values })
    fetch('http://127.0.0.1:5000/api/',{
      method:'POST',
      headers: {
        'Content-type': 'application/json',
      },
      body: JSON.stringify({values}),
    })
    .then(res => res.json())
    .then(res => {
      console.log(res)
      setResponse(res.result)
    }) 
  }
  

  return(
    <div className="App">
      <h2>Employee churn estimation AI (current year)</h2>
      <div>
        <InputForm onSave={handleSubmit}/>
      </div>
      <div>
      {response && <div className='response'>The result is: The employee will <span>{response}</span> in the first year of employment</div>}
      </div>
    </div>
    
   
  )

}

export default App