using Microsoft.EntityFrameworkCore;
// using Domain.Entities;

namespace Infrastructure.Data;

public class ApplicationDbContext : DbContext
{
    public ApplicationDbContext(DbContextOptions<ApplicationDbContext> options)
        : base(options)
    {
    }

    // Hier werden später die DbSet Properties für Ihre Entities hinzugefügt
    // Beispiel: public DbSet<Tournament> Tournaments { get; set; }

    protected override void OnModelCreating(ModelBuilder modelBuilder)
    {
        base.OnModelCreating(modelBuilder);
        
        // Hier können später die Entity-Konfigurationen hinzugefügt werden
    }
} 