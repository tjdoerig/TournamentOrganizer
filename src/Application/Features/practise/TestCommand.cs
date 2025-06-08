using Application.Abstractions.Messaging;

namespace Application.Features.practise;
public record TestCommand(int id, string name) : ICommand;
