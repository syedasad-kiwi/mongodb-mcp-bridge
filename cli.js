#!/usr/bin/env node

const { spawn } = require('child_process');
const path = require('path');

// Get transport type from arguments
const args = process.argv.slice(2);
const transportArg = args.find(arg => arg.startsWith('--transport='));
const transport = transportArg ? transportArg.split('=')[1] : 'stdio';

// Command to run the MCP server
const command = 'mcp';
const serverScript = path.join(__dirname, 'mongodb_mcp_server.py');
const cmdArgs = ['dev', serverScript];

if (transport === 'sse') {
    cmdArgs.push('--transport', 'sse');
}

// Spawn the MCP server process
const serverProcess = spawn(command, cmdArgs, {
    stdio: 'inherit',
    env: { ...process.env }
});

// Handle process events
serverProcess.on('error', (err) => {
    console.error('Failed to start MCP server:', err);
    process.exit(1);
});

serverProcess.on('exit', (code) => {
    process.exit(code);
});

// Handle SIGINT and SIGTERM
process.on('SIGINT', () => serverProcess.kill('SIGINT'));
process.on('SIGTERM', () => serverProcess.kill('SIGTERM'));