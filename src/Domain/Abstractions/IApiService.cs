

namespace Domain.Abstractions;

public interface IApiService
{
    Task<string> SendObjectAsync<T>(T obj, string requestUri, string username, string password);
}