import React,{useState,useEffect} from 'react'
import axios from 'axios'

function App() {
  const [getData,setGetData] = useState()

  useEffect(() => {
    axios.get("http://127.0.0.1:5000/members").then(
      data => {
        setGetData(data.data)
        console.log(data.data)
      }
    )
  },[])
  return(
    <div>
      
      <h1>AMAZON PRODUCT</h1>
      <div>
        {getData!=null?
          getData.map((single) => (
            <div>
            <p>{single.name}</p>
            <p>{single.price}</p>
          <img src={single.image} alt="product picture"/>   
            </div>
          ))

          :
          ""
        }
      </div>

    </div>
  )
}

export default App