﻿using Application.Abstractions.Behaviors;
using Microsoft.Extensions.DependencyInjection;


namespace Application;
public static class DependencyInjection
{
    public static IServiceCollection AddApplication(this IServiceCollection services)
    {
        services.AddMediatR(configuration =>
        {
            configuration.RegisterServicesFromAssembly(typeof(DependencyInjection).Assembly);

            configuration.AddOpenBehavior(typeof(LoggingBehavior<,>));

            configuration.AddOpenBehavior(typeof(ValidationBehavior<,>));
        });

        //services.AddValidatorsFromAssembly(typeof(DependencyInjection).Assembly);


        return services;
    }
}
