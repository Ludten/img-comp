import github from '../../assets/img/github.svg'
import ln from '../../assets/img/linkedin.svg'
import twitter from '../../assets/img/twitter.svg'

const AboutS2 = ()=>{
	return(
		<section className="relative flex h-auto justify-center items-center w-full bg-[#5386DA]">
			<div className='relative flex flex-col w-full items-center h-full max-w-[90rem] my-5 px-10'>
        <div className='relative flex flex-col w-full items-center my-5'>
          <h3 className="font-normal text-4xl text-[#243A5E] my-3">The Team</h3>
          <div className='relative flex flex-col my-5'>
            <div className='relative flex flex-col my-2'>
              <h3 className='flex justify-center font-medium text-2xl text-[#243A5E] my-2'>Mendie Uwemedimo</h3>
              <div className="flex relative space-x-5 items-center justify-center">
                  <a href=""><img src={github} className="w-[100%] h-[100%]"/></a>
                  <a href=""><img src={ln} className="w-[100%] h-[100%]"/></a>
                  <a href=""><img src={twitter} className="w-[60%] h-[100%]"/></a>
              </div>
            </div>
            <div className='relative flex flex-col my-2'>
              <h3 className='flex justify-center font-medium text-2xl text-[#243A5E] my-2'>Damilare John</h3>
              <div className="flex relative space-x-5 items-center justify-center">
                  <a href=""><img src={github} className="w-[100%] h-[100%]"/></a>
                  <a href=""><img src={ln} className="w-[100%] h-[100%]"/></a>
                  <a href=""><img src={twitter} className="w-[60%] h-[100%]"/></a>
              </div>
            </div>
            <div className='relative flex flex-col my-2'>
              <h3 className='flex justify-center font-medium text-2xl text-[#243A5E] my-2'>Oluwateniola Adegbulugbe</h3>
              <div className="flex relative space-x-5 items-center justify-center">
                  <a href=""><img src={github} className="w-[100%] h-[100%]"/></a>
                  <a href=""><img src={ln} className="w-[100%] h-[100%]"/></a>
                  <a href=""><img src={twitter} className="w-[60%] h-[100%]"/></a>
              </div>
            </div>
          </div>
        </div>
      </div>
		</section>
	)
}


export default AboutS2
