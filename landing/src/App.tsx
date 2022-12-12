import { RouterProvider } from "react-router-dom"
import Router from "./routes/index"
import Header from "./common/header"

function App() {

	return (
		<>
			<Header />
			<RouterProvider router={ Router } />
		</>
	)
}

export default App