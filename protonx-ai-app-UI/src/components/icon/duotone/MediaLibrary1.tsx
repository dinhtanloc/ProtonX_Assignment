import React, { SVGProps } from 'react';

const SvgMediaLibrary1 = (props: SVGProps<SVGSVGElement>) => {
	return (
		<svg viewBox='0 0 24 24' className='svg-icon' {...props}>
			<g fill='none' fillRule='evenodd'>
				<path d='M0 0h24v24H0z' />
				<rect fill='currentColor' opacity={0.3} x={2} y={9} width={20} height={13} rx={2} />
				<rect
					fill='currentColor'
					opacity={0.3}
					x={5}
					y={5}
					width={14}
					height={2}
					rx={0.5}
				/>
				<rect
					fill='currentColor'
					opacity={0.3}
					x={7}
					y={1}
					width={10}
					height={2}
					rx={0.5}
				/>
				<path
					d='M10.833 20C9.821 20 9 19.316 9 18.472s.82-1.528 1.833-1.528c.215 0 .42.031.611.087v-4.24c0-.313.196-.59.483-.683l3.514-1.075c.442-.144.892.2.892.684v1.075c0 .358-.335.587-.61.652-.397.095-1.416.299-3.056.612v4.448a.837.837 0 01-.013.152c-.11.757-.883 1.344-1.82 1.344z'
					fill='currentColor'
				/>
			</g>
		</svg>
	);
};

export default SvgMediaLibrary1;
