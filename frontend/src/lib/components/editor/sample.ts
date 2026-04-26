// Default placeholder snippet shown in the editor.
// Built via array-join to avoid Vite/esbuild dep-scanning the literal "import" lines.
export const sampleCode = [
	"import React from 'react';",
	"import { Card } from '@/components/ui/card';",
	'',
	'export default function ArchitecturalCard() {',
	'  return (',
	'    <Card className="glass-panel p-6 border-outline-variant/20 relative overflow-hidden">',
	'      <div className="absolute -right-20 -top-20 w-40 h-40 bg-primary/10 blur-3xl rounded-full pointer-events-none" />',
	'      <h3 className="font-display text-2xl font-bold mb-2">Structural Integrity</h3>',
	'      <p className="text-on-surface-variant text-sm font-body">',
	'        Defining boundaries without lines. Using tonal shifts and negative space.',
	'      </p>',
	'    </Card>',
	'  );',
	'}'
].join('\n');
