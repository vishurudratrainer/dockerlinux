var builder = WebApplication.CreateBuilder(args);

var app = builder.Build();

app.MapGet("/", () => "Hello from ASP.NET Core running inside Docker Compose with PostgreSQL!");

app.Run();