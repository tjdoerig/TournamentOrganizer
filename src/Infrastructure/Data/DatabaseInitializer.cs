using Microsoft.EntityFrameworkCore;

namespace Infrastructure.Data;

public class DatabaseInitializer
{
    private readonly ApplicationDbContext _context;

    public DatabaseInitializer(ApplicationDbContext context)
    {
        _context = context;
    }

    public async Task InitializeDatabaseAsync()
    {
        // Erstellt die Datenbank, falls sie nicht existiert
        await _context.Database.EnsureCreatedAsync();
        
        // Hier können später Initialdaten eingefügt werden
        // Beispiel:
        // if (!await _context.Tournaments.AnyAsync())
        // {
        //     await _context.Tournaments.AddRangeAsync(new List<Tournament> { ... });
        //     await _context.SaveChangesAsync();
        // }
    }
} 