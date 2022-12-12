import { createBrowserRouter } from "react-router-dom"
import type { RouteObject } from "react-router-dom"
import { Landing } from "../pages/main"


const routes: RouteObject[] = [
	{
		path:"/",
		element: <Landing />
	}
]

const router = createBrowserRouter(routes)


export default router
