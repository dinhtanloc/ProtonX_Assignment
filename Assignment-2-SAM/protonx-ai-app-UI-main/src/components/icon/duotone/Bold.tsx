import React, { SVGProps } from 'react';

const SvgBold = (props: SVGProps<SVGSVGElement>) => {
	return (
		<svg viewBox='0 0 24 24' className='svg-icon' {...props}>
			<g fill='none' fillRule='evenodd'>
				<path d='M0 0h24v24H0z' />
				<path
					d='M7.34 19V4.8h5.34c2.32 0 4.22 1.9 4.22 4.22 0 1-.38 1.82-1 2.44 1.2.64 2 1.8 2 3.32 0 2.34-1.9 4.22-4.3 4.22H7.34zm3.2-2.94h2.76c.86 0 1.48-.62 1.48-1.4 0-.78-.62-1.42-1.48-1.42h-2.76v2.82zm0-5.52h1.78c.86 0 1.48-.62 1.48-1.4 0-.78-.62-1.42-1.48-1.42h-1.78v2.82z'
					fill='currentColor'
				/>
			</g>
		</svg>
	);
};

export default SvgBold;
