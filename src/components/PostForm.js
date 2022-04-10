import React, { useState } from 'react';
import axios from 'axios';

function PostForm() {
    const url = 'https://sa-model.herokuapp.com/emotion'
    const [data, setData] = useState({
        msg: ""
    })

    function submit(e){
        e.preventDefault();
        axios.post(url,{
            msg: data.msg,
            withCredentials: true
        })
        .then(res=>{
            console.log(res)
        })
    }

    function handle(e){
        const newData={...data}
        newData[e.target.id] = e.target.value
        setData(newData)
        console.log(newData)
    }

    return (
        <div>
            <form onSubmit={(e)=> submit(e)}>
                <input 
                    onChange={(e) =>handle(e)} id="msg" value={data.msg} placeholder="Enter Sentence" type="text"></input>
                    <button>Submit</button>
            </form>
        </div>
    )
}


export default PostForm