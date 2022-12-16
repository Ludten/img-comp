import comp from "../../assets/img/compression.svg"

const LandingS1 = ()=>{
	return(
    <section className="relative flex h-auto justify-center items-center w-full">
			<div className='relative flex flex-col-reverse sm:flex-row w-full items-center h-full max-w-[90rem] my-10 px-10'>
        <div className="relative flex flex-col w-full sm:w-[50%] items-center justify-center h-[50%] sm:h-full">
          <div className="relative flex flex-col w-[90%] text-center sm:text-left items-center justify-center sm:items-start sm:justify-start">
            <h2 className="my-5 font-medium text-[#3C6AAC] text-3xl md:text-5xl lg:text-7xl">
              Online Image Compression
            </h2>
            <article className="my-5 text-[#898989] font-normal text-base md:text-xl lg:text-2xl">
              Reduce the file size of your images without software installation.
            </article>
            <a href="/project">
              <button className="my-5 border hover:shadow-xl bg-[#AAC2E4] h-14 rounded-xl w-48 text-center text-[#3C6AAC] font-medium text-2xl">Get Started</button>
            </a>
          </div>
        </div>
        <div className="relative flex w-full sm:w-[50%] items-center justify-center h-[50%] sm:h-full">
          <img src={comp} className="w-4/5 h-full"/>
        </div>
      </div>
		</section>
	)
}


export default LandingS1
