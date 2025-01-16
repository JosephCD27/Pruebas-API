import {BrowserRouter, Routes, Route, Navigate} from 'react-router-dom' // importa componentes para enrutamiento
import { TasksPage } from './pages/tasksPage'
import { TasksFormPage } from './pages/taskFormPage'
import {Navigation} from './components/Navigation'
function App() {
  return(
    <BrowserRouter>
      <Navigation />
      <Routes>
        {/* definir las rutas (URLs) */}
        <Route path='/' element={<Navigate to='/tasks' />} />
        <Route path='/tasks' element={<TasksPage />} />
        <Route path='/tasks-create' element={<TasksFormPage />} />
      </Routes>
    </BrowserRouter>
  )
}

export default App
