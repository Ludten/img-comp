import { createBrowserRouter } from "react-router-dom"
import type { RouteObject } from "react-router-dom"
import { Landing, About, Feature } from "../pages/main"


const routes: RouteObject[] = [
	{
		path:"/",
		element: <Landing />
	},
  {
		path:"/about",
		element: <About />
	},
  {
		path:"/features",
		element: <Feature />
	}
]

const router = createBrowserRouter(routes)


export default router
