using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.InteropServices;
using System.Text;
using System.Threading.Tasks;

namespace Domain.Features.practise;
public class Test
{
    public int id { get; set; }
    public string name { get; set; }

    private Test(int id, string name)
    {
        this.id = id;
        this.name = name;
    }

    public static Test Create(int id, string name)
    {
        var test = new Test(id, name);

        return test;
    }

}
