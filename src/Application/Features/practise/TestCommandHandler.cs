using Application.Abstractions.Messaging;
using Domain.Abstractions;
using Domain.Features.practise;
using Microsoft.Extensions.Logging;

namespace Application.Features.practise;
internal sealed class TestCommandHandler : ICommandHandler<TestCommand>
{
    private readonly ITestRepository _testRepository;
    private readonly ILogger<TestCommandHandler> _logger;

    public TestCommandHandler(ITestRepository testRepository, ILogger<TestCommandHandler> logger)
    {
        _testRepository = testRepository;
        _logger = logger;
    }

    public async Task<Result> Handle(TestCommand request, CancellationToken cancellationToken)
    {
        _testRepository.GetById(1);

        _logger.LogWarning("Handler, lalalala");

        await Task.Delay(500);

        return Result.Success();
    }
}
