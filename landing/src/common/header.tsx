import React, { useState } from 'react'
import "../assets/css/header.css"

const Header = ()=>{
  const [nav, setNav] = useState(false);
	return(
		<header className="relative flex h-auto justify-center items-center bg-blue-900 w-full">
			<div className='relative flex flex-col w-full items-center h-full max-w-[90rem] px-5 py-3'>
        <div className='relative flex w-full justify-between items-center'>
          <a href="/">
            <h1
            className='font-extrabold text-lg md:text-2xl text-[#35B0AB]'
            >
              MenComp
            </h1>
          </a>
          <div className='hidden relative w-1/2 sm:flex justify-evenly text-white'>
            <a href="/features" className='flex justify-center items-center'>
              <h3 className="text-lg font-normal">FEATURES</h3>
            </a>
            <a href="/about" className='flex justify-center items-center'>
              <h3 className="text-lg font-normal">ABOUT</h3>
            </a>
            <a href="/project">
              <button className="text-lg w-40 text-center h-10 bg-[#FF725E] border rounded-md font-normal">GET STARTED</button>
            </a>
          </div>
          <div className="block sm:hidden">
            <input type="checkbox" name="hamburger" id="hamburger" className="peer hidden" onChange={ () => setNav(!nav)}/>
            <label htmlFor="hamburger" className="peer-checked:hamburger block relative z-20 p-6 -mr-6 cursor-pointer lg:hidden">
              <div aria-hidden="true" className="m-auto h-0.5 w-6 rounded bg-[#35B0AB] transition duration-300 ease-in-out"></div>
              <div aria-hidden="true" className="m-auto mt-2 h-0.5 w-6 rounded bg-[#35B0AB] transition duration-300 ease-in-out"></div>
            </label>
            <div className={`${nav ? "display:flex" : "hidden"} right-0 h-auto items-center p-5 justify-center absolute bg-white shadow-lg z-[1] flex-col text-black`}>
              <a href="/features" className='relative top-[20%]'>
                <h3 className="text-lg text-center font-normal">FEATURES</h3>
              </a>
              <a href="/about" className='relative top-[20%]'>
                <h3 className="text-lg text-center font-normal">ABOUT</h3>
              </a>
              <a href="/project className='relative top-[20%]'">
                <button className="text-lg w-40 text-center h-10 bg-[#FF725E] border rounded-md font-normal">GET STARTED</button>
              </a>
            </div>
          </div>
        </div>
      </div>
		</header>
	)
}

export default Header
