export function TasksCard({ task }) {
  return (
    <div>
        <h1>{task.titulo}</h1>
        <p>{task.descripcion}</p>
        <hr />
    </div>
  )
}
