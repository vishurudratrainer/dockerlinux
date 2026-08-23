var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

app.MapGet("/", () => "Hello from C# ASP.NET Core!");

app.Run("http://0.0.0.0:8080");