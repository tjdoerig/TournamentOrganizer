using Domain.Features.practise;
using Microsoft.Extensions.Logging;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Infrastructure.Repositories;
public class TestRepository : ITestRepository
{
    private readonly ILogger<TestRepository> _logger;

    public TestRepository(ILogger<TestRepository> logger)
    {
        _logger = logger;
    }

    public Test GetById(int id)
    {
        _logger.LogError("Read from DB, Judihui");

        Random random = new Random();

        var test = Test.Create(random.Next(1, 100), "asdfadf");

        return test;
    }
}
