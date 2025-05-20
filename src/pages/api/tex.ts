import type { NextApiRequest, NextApiResponse } from 'next';

export default function handler(req: NextApiRequest, res: NextApiResponse) {
  const { prompt = '' } = (req.body ?? {}) as { prompt?: string };
  res.status(200).json({ reply: `Echo: ${prompt}` });
}
