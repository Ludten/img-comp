import github from '../../assets/img/git3.svg'

const AboutS3 = ()=>{
	return(
		<section className="relative flex h-auto justify-center items-center w-full">
			<div className='relative flex flex-col w-full items-center h-20 max-w-[90rem] my-10 px-10'>
        <div className='relative flex flex-col w-full items-center justify-center'>
          <a href="" className='relative flex w-full items-center justify-center'>
            <img src={github} className="w-[10%] h-[40%]"/>
            <h3 className="font-normal text-4xl text-[#243A5E] hover:underline px-2">Project Source Code</h3>
          </a>
        </div>
      </div>
		</section>
	)
}


export default AboutS3
