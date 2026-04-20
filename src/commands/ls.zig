const std = @import("std");

pub fn listDir() !void {
    var dir = try std.Io.Dir.cwd().openDir(".", .{ .iterate = true });
    defer dir.close();
    var dirIterator = dir.iterate();
    while (try dirIterator.next()) |dirContent| {
        std.debug.print("{s}\n", .{dirContent.name});
    }
}